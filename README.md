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


The script will process each audio file, extract features, normalize them, and save the normalized features to a CSV file (normalizedfeaturessample.csv).

The script will also store the features in a MongoDB database named audio_features in a collection named features.

Structure

normalizedfeaturessample.csv: Output CSV file containing the normalized features.

fma_sample/: Directory containing the audio files to be processed. Subfolders within this directory will be traversed to find audio files.

Additional Notes

Ensure that the MongoDB server is running locally before running the script. If MongoDB is running on a different host or port, you need to modify the connection string accordingly.


FOR FINDING SIMILAR ITEM PART OF THE CODE

Overview

This PySpark script calculates the similarity between audio files based on their extracted features. It reads normalized audio features from a CSV file, computes the similarity between each pair of audio files using Euclidean distance, and outputs the top 5 similar audio files for each input file.

Requirements

    Python 3.x
    Apache Spark
    PySpark (Python API for Apache Spark)

Usage

Place the normalized features CSV file (normalizedfeaturessample.csv) in the same directory as the script.


The script will compute the similarity between each pair of audio files and output the top 5 similar audio files for each input file in a CSV file named similaraudiosample.csv.

Additional Notes

Ensure that you have a Spark cluster running or have configured Spark to run in standalone mode locally.
The script uses Euclidean distance to calculate similarity between audio files based on their features.
You can modify the script to adjust the similarity metric or change the number of similar files to be output for each input file.


DATASET CAN BE FOUND ON THIS LINK

https://github.com/mdeff/fma

The script utilizes exception handling to skip over files that encounter errors during processing and prints an error message to the console.
You can modify the script to extract additional features or change the normalization technique as needed.
