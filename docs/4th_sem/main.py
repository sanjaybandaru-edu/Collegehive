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
    # print(f"Converting text to audio: {data['text']}")
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




def append_audio_tag(markdown_path, audio_relative_path):
    """Insert an audio HTML tag under the first H1 tag in the markdown file."""
    with open(markdown_path, 'r+', encoding='utf-8') as f:
        content = f.read()
        # Check if audio tag already exists in the content
        if '<audio' in content:
            print(f"Audio tag already exists in Markdown file: {markdown_path}")
            return
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
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', markdown_string)
    # Remove images and links
    text = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', text)  # Remove images
    text = re.sub(r'\[[^\]]*\]\([^)]*\)', '', text)  # Remove Markdown links
    # Headers, lists, bold, italics
    text = re.sub(r'#+\s*(.*?)\s*#*', r'\1', text)  # Convert headers to plain text
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)  # Bold to plain text
    text = re.sub(r'\*(.*?)\*', r'\1', text)  # Italics to plain text
    text = re.sub(r'`{1,3}(.*?)`{1,3}', r'\1', text)  # Code to plain text
    # Remove Markdown tables, detecting them by the presence of lines starting with pipe characters after a header row
    text = re.sub(r'\n\|.*?\|(\n\|[- :|]*\|(\n\|.*?\|)*)', '', text, flags=re.MULTILINE)
    # Convert Markdown lists to plain text lists
    text = re.sub(r'(\n\|.*?\|)+', '', text)  # This attempts to match multiple table rows
    # Remove everything between '---' and '---'
    text = re.sub(r'---.*?---', '', text, flags=re.DOTALL)
    text = re.sub(r'(\$\$)(.*?)(\$\$)', '', text)
    text = text.replace('|', '')
    text = text.replace('%', '')

    # Final whitespace strip
    return text.strip()

# Main function to process directories and handle markdown files
def process_directory(source_directory, target_directory):
    for root, dirs, files in os.walk(source_directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    markdown_content = f.read()
                if not markdown_content:
                    # print(f"Empty file: {file_path}")
                    continue    
                if len(markdown_content.split()) > 750:
                    print(f"Skipped large file: {file_path}")
                    continue
                if '<audio' in markdown_content:
                    print(f"Audio tag already exists in Markdown file: {file_path}")
                    continue
                if "Course Objectives" in markdown_content:
                    print(f"Skipped Syllabus file: {file_path}")
                    continue
                # print(f"Processing file: {file_path}")
                # print(f"Content length: {len(markdown_content.split())}")
                # print(f"Content: {markdown_content}")
                
                

                relative_path = os.path.relpath(root, source_directory)
                target_dir = os.path.join(target_directory, relative_path)
                create_directory_if_not_exists(target_dir)

                audio_file_path = os.path.join(target_dir, file[:-3] + '.mp3')
                audio_relative_path = os.path.relpath(audio_file_path, root)
                convert_text_to_audio(markdown_content, audio_file_path, file_path, audio_relative_path)

if __name__ == "__main__":
    print("Processing started")
    source_directory = 'docs/4th_sem/docs'
    target_directory = 'audio/4th_sem'
    create_directory_if_not_exists(target_directory)
    process_directory(source_directory, target_directory)