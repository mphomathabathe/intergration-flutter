# Google Cloud Flutter and AI Agent Intergration.

<img width="699" alt="Screenshot 2025-03-19 at 21 28 15" src="https://github.com/user-attachments/assets/daf09e0e-039e-4868-9886-4d35a18fe247" />

The purpose of this template is to Integrate a Vertex AI Agent with a Flutter app.

1. Create a search data store and search app using Vertex AI Agent Builder in the Google Cloud console.
2. Deploy a Reasoning Engine agent using Vertex AI Workbench.
3. Use a Python app that integrates with Vertex AI Search and Reasoning Engine agent.
4. Deploy the app to Cloud Run and use it as the backend for a Flutter app.
5. Set up a Firebase project and connect it to the Flutter app.

GCP Usage:  Flutter is used as the client app framework, Vertex AI Search is used as a vector DB, and Reasoning Engine is used to build and deploy an agent with LangChain on Vertex AI. The agent uses Gemini, (LLMs) to generate AI responses to text and image prompts.

## Vertex AI Agent Engine overview (formerly known as LangChain on Vertex AI or Vertex AI Reasoning Engine) 

<img width="850" alt="Screenshot 2025-03-21 at 21 23 56" src="https://github.com/user-attachments/assets/c6a343c0-b9f6-43d2-bb5b-a3d1dc383bdf" />

**Create and deploy on Agent Engine**

<img width="848" alt="Screenshot 2025-03-21 at 21 28 41" src="https://github.com/user-attachments/assets/87de4385-1826-4746-9c50-d01ee0ee41c8" />


Here is a high-level overview of the `app` folder contents:

| Folder/File                         | Description                                                                                                         |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| app                                 | Project root folder that contains the sub-folders and files that make up the Flutter app.                           |
| android/ios/linux/macos/web/windows | Contains platform-specific files that are needed to run the Flutter app on each supported platform.                 |
| lib                                 | Contains the core application Dart files that includes the functionality, routing, data models, and user interface. |
| test                                | Contains Dart tests that are used to test the app's widgets.                                                        |
| pubspec.yaml                        | Contains the app dependencies, Flutter version, and other configuration settings.                                   |
| analysis_options.yaml               | Contains configuration settings for static analysis of the app.                                                     |
