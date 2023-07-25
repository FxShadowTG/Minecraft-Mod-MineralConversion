# -*- coding: utf-8 -*-

import mod.server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()
factory = serverApi.GetEngineCompFactory()

class ChangeOreModServerSystem(ServerSystem):
    def __init__(self, namespace, systemName):
        ServerSystem.__init__(self, namespace, systemName)
        print("服务器准备监听")
        self.ListenEvent()
        print("服务器监听完毕")
        self.levelId = serverApi.GetLevelId()
        self.oreList = [
                        "minecraft:iron_ore",
                        "minecraft:gold_ore",
                        "minecraft:diamond_ore",
                        "minecraft:lapis_ore",
                        "minecraft:redstone_ore",
                        "minecraft:coal_ore",
                        "minecraft:copper_ore",
                        "minecraft:emerald_ore",
                        "minecraft:quartz_ore",
                        "minecraft:nether_gold_ore",
                        "minecraft:ancient_debris",
                        "minecraft:deepslate_iron_ore",
                        "minecraft:deepslate_gold_ore",
                        "minecraft:deepslate_diamond_ore",
                        "minecraft:deepslate_lapis_ore",
                        "minecraft:deepslate_redstone_ore",
                        "minecraft:deepslate_emerald_ore",
                        "minecraft:deepslate_coal_ore",
                        "minecraft:deepslate_copper_ore",
                        "minecraft:raw_iron",
                        "minecraft:raw_gold",
                        "minecraft:raw_copper",
                        ]
        self.oreDict = {
                "minecraft:iron_ore": "minecraft:iron_ingot",
                "minecraft:gold_ore": "minecraft:gold_ingot",
                "minecraft:diamond_ore": "minecraft:diamond",
                "minecraft:lapis_ore": "minecraft:lapis_lazuli",
                "minecraft:redstone_ore": "minecraft:redstone",
                "minecraft:coal_ore": "minecraft:coal",
                "minecraft:copper_ore": "minecraft:copper_ingot",
                "minecraft:emerald_ore": "minecraft:emerald",
                "minecraft:quartz_ore": "minecraft:quartz",
                "minecraft:nether_gold_ore": "minecraft:gold_nugget",
                "minecraft:ancient_debris": "minecraft:netherite_scrap",
                "minecraft:deepslate_iron_ore": "minecraft:raw_iron",
                "minecraft:deepslate_gold_ore": "minecraft:raw_gold",
                "minecraft:deepslate_diamond_ore": "minecraft:diamond",
                "minecraft:deepslate_lapis_ore": "minecraft:lapis_lazuli",
                "minecraft:deepslate_redstone_ore": "minecraft:redstone",
                "minecraft:deepslate_emerald_ore": "minecraft:emerald",
                "minecraft:deepslate_coal_ore": "minecraft:coal",
                "minecraft:deepslate_copper_ore": "minecraft:raw_copper",
                "minecraft:raw_iron": "minecraft:iron_ingot",
                "minecraft:raw_gold": "minecraft:gold_ingot",
                "minecraft:raw_copper": "minecraft:copper_ingot",
        }

    def ListenEvent(self):
        self.ListenForEvent("ChangeOreMod","ChangeOreModClientSystem", "DetectedHoldBeforeClientEvent", self, self.OnDetectedHoldBeforeClientEvent)

    def OnDetectedHoldBeforeClientEvent(self,args):
        print("ok",args)
        playerId = args["__id__"]
        compCreateCommand = factory.CreateCommand(self.levelId)
        compCreateCommand.SetCommand("/playsound block.end_portal.spawn @s",playerId)
        #是否为木棍
        if args["item"] == "minecraft:stick":
            #是的话循环替换玩家背包里的所有物品
            compCreateItem = factory.CreateItem(playerId)
            allItemDict = compCreateItem.GetPlayerAllItems(serverApi.GetMinecraftEnum().ItemPosType.INVENTORY)
            for x in range(36):
                if allItemDict[x] != None and allItemDict[x]["newItemName"] in self.oreList:
                    allItemDict[x]["newItemName"] = self.oreDict[allItemDict[x]["newItemName"]]

            #添加物品
            itemsDictMap = {}
            for i in range(36):
                itemsDictMap[(0, i)] = allItemDict[i]
                compCreateItem.SetPlayerAllItems(itemsDictMap)
            compCreateCommand.SetCommand("/playsound note.flute @s",playerId)
        else:
            #替换玩家手持的物品
            itemDict = {
                'itemName': self.oreDict[args["item"]],
                'count': args["count"],
            }
            compCreateItem = factory.CreateItem(playerId)
            compCreateItem.SpawnItemToPlayerCarried(itemDict,playerId)



    def UnListenEvent(self):
        self.UnListenForEvent("ChangeOreMod","ChangeOreModClientSystem", "DetectedHoldBeforeClientEvent", self, self.OnDetectedHoldBeforeClientEvent)

    def Destroy(self):
        self.UnListenEvent()
        pass
