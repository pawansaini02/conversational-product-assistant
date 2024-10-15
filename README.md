# Generative AI for Conversational Product Assistance

## Overview

The **Generative AI for Conversational Product Assistance** project is a Flask-based web application that leverages OpenAI's GPT-4 to provide intelligent, context-aware responses to user queries about various products. The application supports multimodal input, allowing users to submit both text and images to enhance the interaction.

## Features

- **Conversational AI**: Uses OpenAI's GPT-4 model to generate relevant responses based on user queries.
- **Multimodal Capabilities**: Accepts both text and image inputs. The application can extract information from images, improving the quality of responses.
- **RESTful API**: Exposes an API endpoint for easy integration with front-end applications.

## Technologies Used

- **Backend**: Flask (Python)
- **AI**: OpenAI GPT-4
- **Image Processing**: Pytesseract (for Optical Character Recognition)
- **Environment**: Python 3.x, virtual environment

## Installation

### Prerequisites

- Python 3.x
- OpenAI API key (sign up at [OpenAI](https://platform.openai.com/signup))

### Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/conversational-product-assistant.git
   cd conversational-product-assistant
