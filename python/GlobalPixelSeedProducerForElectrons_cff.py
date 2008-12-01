import FWCore.ParameterSet.Config as cms

import FastSimulation.Tracking.TrajectorySeedProducer_cfi
globalPixelSeedsForElectrons = FastSimulation.Tracking.TrajectorySeedProducer_cfi.trajectorySeedProducer.clone()
globalPixelSeedsForElectrons.firstHitSubDetectorNumber = [2]
globalPixelSeedsForElectrons.firstHitSubDetectors = [1, 2]
globalPixelSeedsForElectrons.secondHitSubDetectorNumber = [2]
globalPixelSeedsForElectrons.secondHitSubDetectors = [1, 2]
globalPixelSeedsForElectrons.seedingAlgo = ['GlobalPixel']
globalPixelSeedsForElectrons.zVertexConstraint = cms.vdouble(0.5)
globalPixelSeedsForElectrons.originRadius = cms.vdouble(0.02)
globalPixelSeedsForElectrons.originpTMin = cms.vdouble(1.5)
