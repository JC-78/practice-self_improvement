//
//  ContentView.swift
//  Nov26_practice
//  Focuses on UI and user interaction


//import SwiftUI

//struct ContentView: View {
//    var body: some View {
//        VStack {
//            Image(systemName: "smiley")
//                .imageScale(.large)
//                .foregroundColor(.accentColor)
//            Text("Hello, world!")
//        }
//        .padding()
//    }
//}
//
//struct ContentView_Previews: PreviewProvider {
//    static var previews: some View {
//        ContentView()
//    }
//}


//
//struct ContentView: View {
//    var body: some View {
//        VStack(spacing: 20) { // Adds spacing between elements
//            Image("test") // Replace "yourImageName" with the actual image asset name
//                .resizable()
//                .scaledToFit()
//                .frame(width: 150, height: 150)
//                .clipShape(Circle()) // Makes the image circular
//                .shadow(radius: 10) // Adds a shadow around the image
//
//            Text("Welcome to My App!")
//                .font(.largeTitle)
//                .fontWeight(.bold)
//                .foregroundColor(.blue)
//
//            Text("This is a simple app to demonstrate a beautiful layout.")
//                .font(.body)
//                .foregroundColor(.gray)
//                .multilineTextAlignment(.center)
//                .padding(.horizontal, 20)
//
//            HStack(spacing: 20) { // Creates a horizontal stack for buttons
//                Button(action: {
//                    print("Like button tapped")
//                }) {
//                    HStack {
//                        Image(systemName: "hand.thumbsup.fill")
//                        Text("Like")
//                    }
//                    .padding()
//                    .background(Color.green)
//                    .foregroundColor(.white)
//                    .cornerRadius(10)
//                }
//
//                Button(action: {
//                    print("Share button tapped")
//                }) {
//                    HStack {
//                        Image(systemName: "square.and.arrow.up")
//                        Text("Share")
//                    }
//                    .padding()
//                    .background(Color.blue)
//                    .foregroundColor(.white)
//                    .cornerRadius(10)
//                }
//            }
//
//            Spacer() // Pushes content to the top
//        }
//        .padding()
//    }
//}
//
//
//struct ContentView_Previews: PreviewProvider {
//    static var previews: some View {
//        ContentView()
//    }
//}
//
//struct ContentView: View {
//    @State private var predictionResult: String = "Prediction will appear here"
//
//    var body: some View {
//        VStack(spacing: 20) {
//            Image("test") // Use your asset image name
//                .resizable()
//                .scaledToFit()
//                .frame(width: 200, height: 200)
//                .clipShape(Circle())
//                .shadow(radius: 10)
//
//            Text(predictionResult)
//                .font(.title)
//                .foregroundColor(.blue)
//                .multilineTextAlignment(.center)
//                .padding()
//
//            Button(action: makePrediction) {
//                Text("Make Prediction")
//                    .padding()
//                    .background(Color.green)
//                    .foregroundColor(.white)
//                    .cornerRadius(10)
//            }
//        }
//        .padding()
//    }
//
//    func makePrediction() {
//        if let inputImage = UIImage(named: "test"),
//           let pixelBuffer = inputImage.toCVPixelBuffer() {
//            do {
//                let prediction = try ModelHandler.shared.predict(from: pixelBuffer)
//                predictionResult = "Prediction: \(prediction)"
//            } catch {
//                predictionResult = "Error: \(error.localizedDescription)"
//            }
//        } else {
//            predictionResult = "Failed to process the image"
//        }
//    }
//}

import SwiftUI
import CoreML
import UIKit

struct ImagePicker: UIViewControllerRepresentable {
    @Binding var image: UIImage?
    
    class Coordinator: NSObject, UIImagePickerControllerDelegate, UINavigationControllerDelegate {
        var parent: ImagePicker
        
        init(parent: ImagePicker) {
            self.parent = parent
        }
        
        func imagePickerControllerDidCancel(_ picker: UIImagePickerController) {
            picker.dismiss(animated: true, completion: nil)
        }
        
        func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [UIImagePickerController.InfoKey : Any]) {
            if let selectedImage = info[.originalImage] as? UIImage {
                parent.image = selectedImage
            }
            picker.dismiss(animated: true, completion: nil)
        }
    }
    
    func makeCoordinator() -> Coordinator {
        return Coordinator(parent: self)
    }
    
    func makeUIViewController(context: Context) -> UIImagePickerController {
        let picker = UIImagePickerController()
        picker.delegate = context.coordinator
        picker.allowsEditing = false // Disable image editing
        picker.sourceType = .photoLibrary // Change to .camera for direct camera access
        return picker
    }
    
    func updateUIViewController(_ uiViewController: UIImagePickerController, context: Context) {
        // No need to update in this case
    }
}


struct ContentView: View {
    @State private var predictionResult: String = "Prediction will appear here"
    @State private var image: UIImage? = nil
    @State private var isImagePickerPresented = false
    
    var body: some View {
        VStack(spacing: 20) {
            if let selectedImage = image {
                Image(uiImage: selectedImage) // Display the captured image
                    .resizable()
                    .scaledToFit()
                    .frame(width: 200, height: 200)
                    .clipShape(Circle())
                    .shadow(radius: 10)
            } else {
                Text("No image selected")
                    .font(.headline)
                    .foregroundColor(.gray)
            }

            Text(predictionResult)
                .font(.title)
                .foregroundColor(.blue)
                .multilineTextAlignment(.center)
                .padding()

            Button(action: {
                isImagePickerPresented = true // Show image picker when tapped
            }) {
                Text("Select Photo")
                    .padding()
                    .background(Color.blue)
                    .foregroundColor(.white)
                    .cornerRadius(10)
            }

            Button(action: makePrediction) {
                Text("Make Prediction")
                    .padding()
                    .background(Color.green)
                    .foregroundColor(.white)
                    .cornerRadius(10)
            }
        }
        .padding()
        .sheet(isPresented: $isImagePickerPresented) {
            ImagePicker(image: $image) // ImagePicker view for selecting a photo
        }
    }
    
    func makePrediction() {
        guard let selectedImage = image,
              let pixelBuffer = selectedImage.toCVPixelBuffer() else {
            predictionResult = "Failed to process the image"
            return
        }
        
        do {
            let prediction = try ModelHandler.shared.predict(from: pixelBuffer)
            predictionResult = "Prediction: \(prediction)"
        } catch {
            predictionResult = "Error: \(error.localizedDescription)"
        }
    }
}



