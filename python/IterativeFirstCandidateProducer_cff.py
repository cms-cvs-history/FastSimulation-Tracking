import FWCore.ParameterSet.Config as cms

import FastSimulation.Tracking.TrackCandidateProducer_cfi
iterativeFirstTrackCandidatesWithTriplets = FastSimulation.Tracking.TrackCandidateProducer_cfi.trackCandidateProducer.clone()
import FastSimulation.Tracking.TrackCandidateProducer_cfi
iterativeFirstTrackCandidatesWithPairs = FastSimulation.Tracking.TrackCandidateProducer_cfi.trackCandidateProducer.clone()
iterativeFirstTrackCandidates = cms.Sequence(iterativeFirstTrackCandidatesWithTriplets+iterativeFirstTrackCandidatesWithPairs)
iterativeFirstTrackCandidatesWithTriplets.SeedProducer = cms.InputTag("iterativeFirstSeeds","FirstPixelTriplets")
iterativeFirstTrackCandidatesWithTriplets.TrackProducers = ['globalPixelWithMaterialTracks']
iterativeFirstTrackCandidatesWithTriplets.MinNumberOfCrossedLayers = 5
iterativeFirstTrackCandidatesWithPairs.SeedProducer = cms.InputTag("iterativeFirstSeeds","FirstMixedPairs")
iterativeFirstTrackCandidatesWithPairs.TrackProducers = ['globalPixelWithMaterialTracks']
iterativeFirstTrackCandidatesWithPairs.MinNumberOfCrossedLayers = 5

