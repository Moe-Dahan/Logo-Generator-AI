# Logo-Generator-AI

This is a simple Python script for generating logos using the Hugging Face FLUX.1-dev model. By providing a text prompt, the script generates a logo image and saves it as `logo.png`.

## Features
- Converts user-provided text prompts into logo designs.
- Leverages the Hugging Face FLUX.1-dev model for text-to-image generation.
- Saves the generated logo as a `.png` file.

## Prerequisites
To run this script, ensure you have the following installed:

1. **Python 3.7 or later**
2. **Required Python Libraries:**
   - `requests`
   - `Pillow`

Install the libraries using pip:
```bash
pip install requests pillow
```

3. **Hugging Face API Key**
   - Sign up or log in to [Hugging Face](https://huggingface.co/) to get your API key.

## Usage

1. Clone or download this repository to your local machine.
2. Open the script and replace `hf_your_api_key` in the `headers` dictionary with your actual Hugging Face API key.
3. Run the script:
```bash
python logo_generator.py
```
4. Enter a descriptive prompt for your logo when prompted (e.g., `"A sleek and modern logo for a tech startup with clean lines and blue accents."`).
5. The generated logo will be saved as `logo.png` in the current directory.



## Customization
You can customize the following parameters in the script:
- `target_size`: Adjust the dimensions of the generated image.
- `guidance_scale`: Modify the influence of your prompt on the generated image.

## Notes
- Ensure your API key is valid and has sufficient access to use the specified model.
- The script uses `x-wait-for-model` to ensure synchronous execution, which may cause slight delays if the model is loading.

## License
This project is open-source and available under the MIT License.

## Support
If you encounter any issues or have questions, feel free to raise an issue or contact the developer.

