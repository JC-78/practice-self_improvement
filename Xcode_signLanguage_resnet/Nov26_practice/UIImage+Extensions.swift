//
//  UIImage+Extensions.swift
//  Reusable code for image preprocessing

import UIKit
import CoreML
//
//extension UIImage {
//    func toCVPixelBuffer() -> CVPixelBuffer? {
//        let width = 200 //224
//        let height = 200 //224
//        let attributes: [NSObject: AnyObject] = [
//            kCVPixelBufferCGImageCompatibilityKey: true as AnyObject,
//            kCVPixelBufferCGBitmapContextCompatibilityKey: true as AnyObject
//        ]
//        var pixelBuffer: CVPixelBuffer?
//        let status = CVPixelBufferCreate(kCFAllocatorDefault, width, height,
//                                         kCVPixelFormatType_32ARGB, attributes as CFDictionary, &pixelBuffer)
//        guard status == kCVReturnSuccess, let resultPixelBuffer = pixelBuffer else {
//            return nil
//        }
//
//        CVPixelBufferLockBaseAddress(resultPixelBuffer, CVPixelBufferLockFlags(rawValue: 0))
//        let data = CVPixelBufferGetBaseAddress(resultPixelBuffer)
//        let rgbColorSpace = CGColorSpaceCreateDeviceRGB()
//        let context = CGContext(data: data, width: width, height: height,
//                                bitsPerComponent: 8, bytesPerRow: CVPixelBufferGetBytesPerRow(resultPixelBuffer),
//                                space: rgbColorSpace,
//                                bitmapInfo: CGImageAlphaInfo.noneSkipFirst.rawValue)
//        guard let cgImage = self.cgImage else {
//            return nil
//        }
//        context?.draw(cgImage, in: CGRect(x: 0, y: 0, width: width, height: height))
//        CVPixelBufferUnlockBaseAddress(resultPixelBuffer, CVPixelBufferLockFlags(rawValue: 0))
//        return resultPixelBuffer
//    }
//}
import UIKit
import CoreVideo

extension UIImage {
    func toCVPixelBuffer() -> CVPixelBuffer? {
        // Resize the image to 200x200 before converting it to a pixel buffer
        let resizedImage = self.resized(to: CGSize(width: 200, height: 200))
        
        guard let cgImage = resizedImage.cgImage else { return nil }
        
        let attrs = [
            kCVPixelBufferCGImageCompatibilityKey: true,
            kCVPixelBufferCGBitmapContextCompatibilityKey: true
        ] as CFDictionary
        
        var pixelBuffer: CVPixelBuffer?
        let status = CVPixelBufferCreate(kCFAllocatorDefault, 200, 200, kCVPixelFormatType_32ARGB, attrs, &pixelBuffer)
        
        guard status == kCVReturnSuccess, let resultPixelBuffer = pixelBuffer else {
            return nil
        }
        
        CVPixelBufferLockBaseAddress(resultPixelBuffer, [])
        
        let context = CGContext(data: CVPixelBufferGetBaseAddress(resultPixelBuffer),
                                width: 200,
                                height: 200,
                                bitsPerComponent: 8,
                                bytesPerRow: CVPixelBufferGetBytesPerRow(resultPixelBuffer),
                                space: CGColorSpaceCreateDeviceRGB(),
                                bitmapInfo: CGImageAlphaInfo.noneSkipFirst.rawValue)
        
        context?.draw(cgImage, in: CGRect(x: 0, y: 0, width: 200, height: 200))
        
        CVPixelBufferUnlockBaseAddress(resultPixelBuffer, [])
        
        return resultPixelBuffer
    }
    
    // Helper function to resize the image
    func resized(to size: CGSize) -> UIImage {
        UIGraphicsBeginImageContextWithOptions(size, false, self.scale)
        self.draw(in: CGRect(origin: .zero, size: size))
        let resizedImage = UIGraphicsGetImageFromCurrentImageContext()
        UIGraphicsEndImageContext()
        return resizedImage ?? self
    }
}
