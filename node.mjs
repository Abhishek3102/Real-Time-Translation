import readline from 'readline';
import gta from '@vitalets/google-translate-api';

const { translate } = gta;

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

async function askUserAndTranslate() {
  rl.question('Enter the text to translate: ', async (inputText) => {
    try {
      // Ask the user for the source language
      rl.question('Enter the language code of the original text (e.g., "en" for English): ', async (sourceLang) => {
        // Ask the user for the target language
        rl.question('Enter the language code to translate to (e.g., "fr" for French): ', async (targetLang) => {
          // Perform the translation
          const result = await translate(inputText, { from: sourceLang, to: targetLang });
          console.log(`Translated text from ${sourceLang} to ${targetLang}:`, result.text);
          rl.close();
        });
      });
    } catch (error) {
      console.error('Error during translation:', error);
      rl.close();
    }
  });
}

askUserAndTranslate();




// import { translate } from '@vitalets/google-translate-api';
// import { HttpProxyAgent } from 'http-proxy-agent';

// const agent = new HttpProxyAgent('http://proxy.example.com:8080');
// translate('Привет, мир!', {
//   to: 'en',
//   fetchOptions: { agent },
// }).then(({ text }) => {
//   console.log('Translated text:', text);
// }).catch(error => {
//   console.error('Translation error:', error);
// });
