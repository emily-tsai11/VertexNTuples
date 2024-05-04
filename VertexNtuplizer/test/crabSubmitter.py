from CRABClient.UserUtilities import config
config = config()

sample = "TTToHadronic_noPU"
# sample = "TTToHadronic_PU200"

config.General.requestName       = sample
config.General.workArea          = "/eos/user/e/etsai/workspace/VertexNtuples_CMSSW_14_1_0_pre3/src/VertexNtuples/VertexNtuplizer/test"
config.General.transferOutputs   = True
config.General.instance          = "prod"

config.JobType.pluginName        = "Analysis"
config.JobType.psetName          = "VertexNtuplizer.py"
config.JobType.maxMemoryMB       = 3000
config.JobType.maxJobRuntimeMin  = 60

config.Data.splitting            = "FileBased"
config.Data.unitsPerJob          = 1
config.Data.outLFNDirBase        = "/store/user/etsai"
config.Data.publication          = False
config.Data.outputDatasetTag     = sample
config.Data.userInputFiles       = open(sample + ".list").readlines()
config.Data.outputPrimaryDataset = "VertexNtuples"

config.Site.storageSite          = "T2_CH_CERN"
config.Site.whitelist            = ["T2_CH_CERN"]
