# -*- coding: utf-8 -*-

from mod.common.mod import Mod
import mod.server.extraServerApi as serverApi
import mod.client.extraClientApi as clientApi

@Mod.Binding(name="ChangeOreMod", version="0.0.1")
class ChangeOreMod(object):

    def __init__(self):
        pass

    @Mod.InitServer()
    def ChangeOreModServerInit(self):
        serverApi.RegisterSystem("ChangeOreMod","ChangeOreModServerSystem","ChangeOreMod.ChangeOreModServerSystem.ChangeOreModServerSystem")
        print("服务注册成功")

    @Mod.DestroyServer()
    def ChangeOreModServerDestroy(self):
        print("服务销毁成功")

    @Mod.InitClient()
    def ChangeOreModClientInit(self):
        clientApi.RegisterSystem("ChangeOreMod","ChangeOreModClientSystem","ChangeOreMod.ChangeOreModClientSystem.ChangeOreModClientSystem")
        print("客户注册成功")

    @Mod.DestroyClient()
    def ChangeOreModClientDestroy(self):
        print("客户销毁成功")
