//
//  ModelHandler.swift
//Encapsulates Core ML logic, making it easier to update or replace the model.
import UIKit
import CoreML
//
//class ModelHandler {
//    static let shared = ModelHandler()
//    private let model: model_resnet18_200//ResNet // Replace `ResNet` with your actual model class name
//
//    private init() {
//        model = try! model_resnet18_200() //ResNet() // Initialize your Core ML model
//    }
//
//    func predict(from pixelBuffer: CVPixelBuffer) throws -> String {
//        let output = try model.prediction(input: pixelBuffer)
//        return output.classLabel // Adjust according to your model's output structure
//    }
//}

class ModelHandler {
    static let shared = ModelHandler()
    private let model: model_resnet18_200 // Replace with your actual model class name

    private init() {
        model = try! model_resnet18_200() // Initialize your Core ML model
    }
    
    func predict(from pixelBuffer: CVPixelBuffer) throws -> String {
        // Wrap the CVPixelBuffer in a `model_resnet18_200Input` object
        let input = model_resnet18_200Input(image: pixelBuffer) // Check the auto-generated input label in your Core ML model
        let output = try model.prediction(input: input)
        
        // Access the classLabel or other outputs based on the model's structure
        return output.classLabel // Adjust this based on your model's output properties
    }
}
