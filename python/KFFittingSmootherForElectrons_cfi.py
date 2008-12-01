import FWCore.ParameterSet.Config as cms

KFFittingSmootherForElectrons = cms.ESProducer(
    "KFFittingSmootherESProducer",
    EstimateCut = cms.double(30.0),
    Fitter = cms.string('KFFitter'),
    MinNumberOfHits = cms.int32(5),
    Smoother = cms.string('KFSmoother'),
    BreakTrajWith2ConsecutiveMissing = cms.bool(True),
    ComponentName = cms.string('KFFittingSmootherForElectrons'),
    NoInvalidHitsBeginEnd = cms.bool(True),
    RejectTracks = cms.bool(True)
)