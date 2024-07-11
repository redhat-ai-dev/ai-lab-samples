ROOT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )" 

CHATBOT_DIR=$ROOT_DIR/chatbot
CODEGEN_DIR=$ROOT_DIR/codegen
AUDIO_TO_TEXT_DIR=$ROOT_DIR/audio-to-text

REPO="https://github.com/containers/ai-lab-recipes"

TEMPDIR=$ROOT_DIR/temp
rm -rf $TEMPDIR # clean up
mkdir -p $TEMPDIR
cd $TEMPDIR
git clone $REPO 2>&1 > /dev/null

REPONAME=$(basename $REPO)

cp -r $TEMPDIR/$REPONAME/recipes/natural_language_processing/chatbot/app/ $CHATBOT_DIR/
cp -r $TEMPDIR/$REPONAME/recipes/natural_language_processing/codegen/app/ $CODEGEN_DIR/
cp -r $TEMPDIR/$REPONAME/recipes/audio/audio_to_text/app/ $AUDIO_TO_TEXT_DIR/  

rm -rf $TEMPDIR # clean up