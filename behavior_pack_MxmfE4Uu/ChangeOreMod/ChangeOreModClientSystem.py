# -*- coding: utf-8 -*-

import mod.client.extraClientApi as clientApi
ClientSystem = clientApi.GetClientSystemCls()
factory = clientApi.GetEngineCompFactory()

class ChangeOreModClientSystem(ClientSystem):
    def __init__(self, namespace, systemName):
        ClientSystem.__init__(self, namespace, systemName)
        print("客户端准备监听")
        self.ListenEvent()
        print("客户端监听完毕")
        self.levelId = clientApi.GetLevelId()
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
                        "minecraft:stick",
                        ]
        
    def ListenEvent(self):
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), "HoldBeforeClientEvent", self, self.OnHoldBeforeClientEvent)

    def OnHoldBeforeClientEvent(self,args):
        print("收到长按")
        playerId = clientApi.GetLocalPlayerId()
        #获取游戏模式
        compCreateGame = factory.CreateGame(self.levelId)
        gameType = compCreateGame.GetPlayerGameType(playerId)
        #如果不为生存模式则失效
        if gameType != 0:
            return
        #检测潜行
        compCreatePlayer = factory.CreatePlayer(playerId)
        is_sneaking = compCreatePlayer.isSneaking()
        if is_sneaking == True:
            compCreateItem = factory.CreateItem(playerId)
            carriedData = compCreateItem.GetCarriedItem(True)
            print(carriedData)
            #过滤矿物和木棍
            if carriedData["newItemName"] in self.oreList:
                print("过滤通过")
                self.NotifyToServer("DetectedHoldBeforeClientEvent", {"item": carriedData["newItemName"],"count": carriedData["count"]})

    def UnListenEvent(self):
        self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), "HoldBeforeClientEvent", self, self.OnHoldBeforeClientEvent)

    def Destroy(self):
        self.UnListenEvent()
        pass

