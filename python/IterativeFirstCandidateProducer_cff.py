import FWCore.ParameterSet.Config as cms

import copy
from FastSimulation.Tracking.TrackCandidateProducer_cfi import *
iterativeFirstTrackCandidatesWithTriplets = copy.deepcopy(trackCandidateProducer)
import copy
from FastSimulation.Tracking.TrackCandidateProducer_cfi import *
iterativeFirstTrackCandidatesWithPairs = copy.deepcopy(trackCandidateProducer)
iterativeFirstTrackCandidates = cms.Sequence(iterativeFirstTrackCandidatesWithTriplets+iterativeFirstTrackCandidatesWithPairs)
iterativeFirstTrackCandidatesWithTriplets.SeedProducer = cms.InputTag("iterativeTrackingSeeds","FirstMixedTriplets")
iterativeFirstTrackCandidatesWithTriplets.TrackProducer = 'globalPixelGSWithMaterialTracks'
iterativeFirstTrackCandidatesWithTriplets.MinNumberOfCrossedLayers = 5
iterativeFirstTrackCandidatesWithPairs.SeedProducer = cms.InputTag("iterativeTrackingSeeds","FirstMixedPairs")
iterativeFirstTrackCandidatesWithPairs.TrackProducer = 'globalPixelGSWithMaterialTracks'
iterativeFirstTrackCandidatesWithPairs.MinNumberOfCrossedLayers = 5

