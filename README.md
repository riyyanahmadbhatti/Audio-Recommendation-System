FOR PREPROCESSING PART OF CODE

Audio Feature Extraction and Storage

Overview

This Python script extracts audio features from a collection of audio files, normalizes them, and then stores them in both a CSV file and a MongoDB database. The extracted features include Mel-Frequency Cepstral Coefficients (MFCCs), Spectral Centroid, and Zero Crossing Rate.

Requirements

    Python 3.x
    Libraries:
        os
        librosa
        numpy
        scikit-learn (for StandardScaler)
        csv
        pymongo

Usage

    Place your audio files in the directory specified in the mainaudiofolder variable. Make sure the audio files are in .mp3 format.

    Run the script audio_feature_extraction.py.

python audio_feature_extraction.py

The script will process each audio file, extract features, normalize them, and save the normalized features to a CSV file (normalizedfeaturessample.csv).

The script will also store the features in a MongoDB database named audio_features in a collection named features.

Structure

    audio_feature_extraction.py: Main Python script containing the feature extraction, normalization, CSV writing, and MongoDB insertion logic.
    normalizedfeaturessample.csv: Output CSV file containing the normalized features.
    fma_sample/: Directory containing the audio files to be processed. Subfolders within this directory will be traversed to find audio files.

Additional Notes

    Ensure that the MongoDB server is running locally before running the script. If MongoDB is running on a different host or port, you need to modify the connection string accordingly.
    The script utilizes exception handling to skip over files that encounter errors during processing and prints an error message to the console.
    You can modify the script to extract additional features or change the normalization technique as needed.
