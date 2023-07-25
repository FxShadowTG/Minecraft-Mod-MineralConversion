# -*- coding: utf-8 -*-

from mod.common.mod import Mod


@Mod.Binding(name="Script_NeteaseModAGzxjMBQ", version="0.0.1")
class Script_NeteaseModAGzxjMBQ(object):

    def __init__(self):
        pass

    @Mod.InitServer()
    def Script_NeteaseModAGzxjMBQServerInit(self):
        pass

    @Mod.DestroyServer()
    def Script_NeteaseModAGzxjMBQServerDestroy(self):
        pass

    @Mod.InitClient()
    def Script_NeteaseModAGzxjMBQClientInit(self):
        pass

    @Mod.DestroyClient()
    def Script_NeteaseModAGzxjMBQClientDestroy(self):
        pass
