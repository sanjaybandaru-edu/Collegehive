import requests
import re
import os

# Function to create directories if they do not exist
def create_directory_if_not_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created directory: {path}")

# Function to convert text to audio and handle file operations
def convert_text_to_audio(text, target_file_path, markdown_path, audio_relative_path):
    url = 'https://4336zvnmaw.us-east-1.awsapprunner.com/convert'
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json',
        'Origin': 'https://beta.meetaugie.com'
    }
    data = {"voiceId": "wRTEg58D7p7fc9Knory0", "text": markdown_to_plain_text(text)}
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 201:
        mp3_url = response.json()['contentUrl']
        mp3_response = requests.get(mp3_url)
        if mp3_response.status_code == 200:
            with open(target_file_path, 'wb') as f:
                f.write(mp3_response.content)
            print(f"Audio file saved: {target_file_path}")
            append_audio_tag(markdown_path, audio_relative_path)
        else:
            print("Failed to download the MP3 file")
    else:
        print("Failed to convert text to audio")

# Function to append an audio tag to the markdown file
# def append_audio_tag(markdown_path, audio_relative_path):
#     # audio_tag = f'<audio controls style="width: 100%;"><source src="{audio_relative_path}" type="audio/mpeg">Your browser does not support the audio element.</audio>'
#     # with open(markdown_path, 'a') as md_file:
#     #     md_file.write("\n" + audio_tag)
#     """Insert an audio HTML tag under the first H1 tag in the markdown file."""
#     with open(markdown_path, 'r+', encoding='utf-8') as f:
#         content = f.read()
#         # Safely replace to avoid escape issues
#         audio_tag = f'''\n\n<audio controls style="width: 100%;">\n  <source src="{audio_relative_path}" type="audio/mpeg">\n  Your browser does not support the audio element.\n</audio>\n\n'''
#         print(audio_tag)
#         content = re.sub(r'(#[^#\n]+)\n', r'\1' + audio_tag, content, 1)
#         f.seek(0)
#         f.write(content)
#         f.truncate()
#         print(f"Updated Markdown file with audio link: {markdown_path}")




def append_audio_tag(markdown_path, audio_relative_path):
    """Insert an audio HTML tag under the first H1 tag in the markdown file."""
    with open(markdown_path, 'r+', encoding='utf-8') as f:
        content = f.read()
        # Define the audio_tag with escaped backslashes for HTML and file paths
        audio_tag = (
            r'\n\n<audio controls style="width: 100%;">\n  '
            r'<source src="' + audio_relative_path.replace('\\', '\\\\') + r'" type="audio/mpeg">\n  '
            r'Your browser does not support the audio element.\n</audio>\n\n'
        )
        # Use re.sub to insert the audio tag; escape backslashes in replacement string
        content = re.sub(r'(#[^#\n]+)\n', r'\1' + audio_tag, content, 1)
        f.seek(0)
        f.write(content)
        f.truncate()
        print(f"Updated Markdown file with audio link: {markdown_path}")


# Helper function to convert markdown text to plain text
def markdown_to_plain_text(markdown_string):
    # Example regexes for simplifying markdown; you may need to customize these
    no_images = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', markdown_string)
    no_links = re.sub(r'\[[^\]]*\]\([^)]*\)', '', no_images)
    plain_text = re.sub(r'#', '', no_links)
    return plain_text.strip()

# Main function to process directories and handle markdown files
def process_directory(source_directory, target_directory):
    for root, dirs, files in os.walk(source_directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    markdown_content = f.read()

                relative_path = os.path.relpath(root, source_directory)
                target_dir = os.path.join(target_directory, relative_path)
                create_directory_if_not_exists(target_dir)

                audio_file_path = os.path.join(target_dir, file[:-3] + '.mp3')
                audio_relative_path = os.path.relpath(audio_file_path, root)
                convert_text_to_audio(markdown_content, audio_file_path, file_path, audio_relative_path)

if __name__ == "__main__":
    print("Processing started")
    source_directory = 'GB/Unit-1 Introduction to Global Business'
    target_directory = 'audio/GB/Unit-1 Introduction to Global Business'
    create_directory_if_not_exists(target_directory)
    process_directory(source_directory, target_directory)