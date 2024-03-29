# Image Blending Lambda

This AWS Lambda function receives two URL-encoded image URLs as parameters, downloads the images, overlays them, and returns the resulting image. You can use the URL generated by this function in an `<img>` tag in your web application to display the combined image.

## Usage

### Parameters

The function expects two parameters in the URL:

- `img1`: URL of the first image (URL-encoded format).
- `img2`: URL of the second image (URL-encoded format).

Example call:

```html
<img src="https://example.com/lambda?img1=https://img.com/img.png&img2=https://img.com/img1.png"/>
```

## Response

The function returns the resulting image in PNG format. Make sure to use the URL generated by the function in the `<img src="">` tag of your web application.


## Configuration

### Required Packages

- `Pillow`: Ensure you include this package when packaging your Lambda function.

### Code Example

The code for the Lambda function is in the `lambda_function.py`file. Make sure to package the code along with the required packages when creating your Lambda function.

## Local Development

If you want to test the function locally, you can use tools like `lambda-local`. Ensure you install the dependencies before running it locally.

```
pip install Pillow
pip install lambda-local
lambda-local -f lambda_function.lambda_handler -t 300 -e event.json
```