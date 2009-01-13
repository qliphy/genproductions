import FWCore.ParameterSet.Config as cms

process = cms.Process('LHE')

# import of standard configurations
process.load('FWCore/MessageService/MessageLogger_cfi')

process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.2 $'),
    annotation = cms.untracked.string('MadGraph single top t channel at 10TeV'),
    name = cms.untracked.string('$Source: /cvs_server/repositories/CMSSW/CMSSW/Configuration/GenProduction/python/MCDBSource_SingleTop_t_10TeV_FastSim_cff.py,v $')
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.options = cms.untracked.PSet(
    Rethrow = cms.untracked.vstring('ProductNotFound')
)

# Input source

process.source = cms.Source("MCDBSource",
    articleID = cms.uint32(216),
    supportedProtocols = cms.vstring('rfio')
)

# direct CASTOR path
#process.source = cms.Source("LHESource",
#    fileNames = cms.untracked.vstring("rfio:///castor/cern.ch/sft/mcdb/storage/216/MadGraph_10TeV_tchannel.lhe")
#)    

# Output definition
process.output = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('MCDBSource_SingleTop_t_10TeV_cff_py_LHE.root'),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('USER'),
        filterName = cms.untracked.string('')
    )
)

# Additional output definition

# Other statements

# Path and EndPath definitions
process.out_step = cms.EndPath(process.output)

# Schedule definition
process.schedule = cms.Schedule(process.out_step)
