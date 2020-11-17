from Configuration.StandardSequences.Eras import eras

process = cms.Process('MERGE')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10000)
)

# Input source
process.source = cms.Source("PoolSource",
    duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
    dropDescendantsOfDroppedBranches = cms.untracked.bool(False),
    fileNames = cms.untracked.vstring(
        "file:file1.root",
        "file:file2.root",
        "file:file3.root",
        ),
)

process.options = cms.untracked.PSet(

)

# Output definition
process.output = cms.OutputModule("PoolOutputModule",
                                  fileName = cms.untracked.string("outputFile.root")
                                  )

process.ep = cms.EndPath(process.output)

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 500
