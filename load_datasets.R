# Install once if needed:
install.packages("googledrive")
install.packages("readr")

library(googledrive)
library(readr)


# --- load_datasets.R ---

library(googledrive)
library(readr)

# Google Drive file IDs (same mapping as your Python code)
files <- list(
  training   = "1PT-8M-Nbw8aBGXXdonN7QCe59AqEBYOs",
  test       = "1y0OcL5_S0PtJW2aeUq5Qm7cy6ehdfuob",
  validation = "1o_211YxzPtY2_Gz2d9xRfOALu7AjPzF_"
)

download_and_load_csv <- function(file_id, name) {
  filename <- paste0(name, "_dataset.csv")
  
  # Download if file does not exist
  if (!file.exists(filename)) {
    message(sprintf("⬇ Downloading %s dataset from Google Drive...", name))
    drive_download(as_id(file_id), path = filename, overwrite = TRUE)
  } else {
    message(sprintf("%s already exists.", filename))
  }
  
  # Read CSV
  tryCatch({
    read_csv(filename, show_col_types = FALSE)
  }, error = function(e) {
    stop(sprintf("Could not load %s as CSV: %s", filename, e$message))
  })
}

load_all_datasets <- function() {
  datasets <- list()
  for (name in names(files)) {
    datasets[[name]] <- download_and_load_csv(files[[name]], name)
  }
  datasets
}
