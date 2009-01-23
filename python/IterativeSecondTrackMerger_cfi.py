import FWCore.ParameterSet.Config as cms

iterativeSecondTrackMerging = cms.EDFilter("FastTrackMerger",
    TrackProducers = cms.VInputTag(cms.InputTag("iterativeSecondTrackCandidatesWithTriplets"),
                                   cms.InputTag("iterativeSecondTracksWithTriplets")),
    trackAlgo = cms.untracked.uint32(2)
)



