import kagglehub

# Download selected version
path = kagglehub.dataset_download("andrewmvd/brazilian-stock-market/versions/840")

print("Path to dataset files:", path)
