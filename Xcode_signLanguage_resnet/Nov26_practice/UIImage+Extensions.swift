//
//  UIImage+Extensions.swift
//  Reusable code for image preprocessing

import UIKit
import CoreML

extension UIImage {
    func toCVPixelBuffer() -> CVPixelBuffer? {
        let width = 200 //224
        let height = 200 //224
        let attributes: [NSObject: AnyObject] = [
            kCVPixelBufferCGImageCompatibilityKey: true as AnyObject,
            kCVPixelBufferCGBitmapContextCompatibilityKey: true as AnyObject
        ]
        var pixelBuffer: CVPixelBuffer?
        let status = CVPixelBufferCreate(kCFAllocatorDefault, width, height,
                                         kCVPixelFormatType_32ARGB, attributes as CFDictionary, &pixelBuffer)
        guard status == kCVReturnSuccess, let resultPixelBuffer = pixelBuffer else {
            return nil
        }

        CVPixelBufferLockBaseAddress(resultPixelBuffer, CVPixelBufferLockFlags(rawValue: 0))
        let data = CVPixelBufferGetBaseAddress(resultPixelBuffer)
        let rgbColorSpace = CGColorSpaceCreateDeviceRGB()
        let context = CGContext(data: data, width: width, height: height,
                                bitsPerComponent: 8, bytesPerRow: CVPixelBufferGetBytesPerRow(resultPixelBuffer),
                                space: rgbColorSpace,
                                bitmapInfo: CGImageAlphaInfo.noneSkipFirst.rawValue)
        guard let cgImage = self.cgImage else {
            return nil
        }
        context?.draw(cgImage, in: CGRect(x: 0, y: 0, width: width, height: height))
        CVPixelBufferUnlockBaseAddress(resultPixelBuffer, CVPixelBufferLockFlags(rawValue: 0))
        return resultPixelBuffer
    }
}
