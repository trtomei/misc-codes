import FWCore.ParameterSet.Config as cms

process = cms.Process("PRINT")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(20)
)

# Input source
process.source = cms.Source("PoolSource",
    duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
    dropDescendantsOfDroppedBranches = cms.untracked.bool(False),
    fileNames = cms.untracked.vstring(
        "file:file.root",
        ),
)

process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")

# Example: print Z bosons and their daughters
process.ZAndChildren = cms.EDProducer(
    "GenParticlePruner",
    src = cms.InputTag("prunedGenParticles"),
    select = cms.vstring(
    "drop  *  ", # this is the default
    "keep+ pdgId = {Z0}",
    "drop pdgId = {Z0} & status = 2"
    )
)

process.printTree = cms.EDAnalyzer("ParticleListDrawer",
                                   maxEventsToPrint = cms.untracked.int32(20),
                                   printVertex = cms.untracked.bool(False),
                                   printOnlyHardInteraction = cms.untracked.bool(False), 
                                   # Print only status=3 particles. This will not work for Pythia8, which does not have any such particles.
                                   src = cms.InputTag("ZAndChildren")
                                   )

process.p = cms.Path(process.ZAndChildren+process.printTree)