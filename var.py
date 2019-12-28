import queue


pvaPath = "pva.xlsx"
messagePath = "message.xlsx"

info = list()
infoLen = int()
threadCount = 0
browserSelect = "Chrome"
typeSelect = "activity"

proxyUser = "lum-customer-rubelrana-zone-rubel3"
proxyPassword = "8fcx425tcd6k"

terminate = False
pause = False
monitorQ = queue.Queue()
infoQ = queue.Queue()