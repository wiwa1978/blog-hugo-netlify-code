const { BotkitConversation } = require("botkit");
const axios = require("axios");

module.exports = function(controller) {
    const convo = new BotkitConversation('chat', controller);

    convo.before('default', async(convo, bot) => {
        axios.get('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1') 
            .then(function (response) {
                convo.setVar('deck_id', response.data.deck_id);
                console.log(response.data.deck_id);
              
            })
        .catch(function (error) {
            console.log(error);
        })
    });

    convo.ask('What is your name?', async(response, convo, bot) => {
        console.log(`The name is ${ response }`);
      }, 'name');
    convo.addAction('msg');
    convo.addMessage('Hi {{vars.name}}! Let us play a small card game', 'msg');
    convo.addMessage('Your deck is shuffled and has id {{vars.deck_id}}', 'msg');
    
    controller.addDialog( convo );

    controller.hears( 'deck', 'message,direct_message', async ( bot, message ) => {
        await bot.beginDialog( 'chat' );
    });

    controller.commandHelp.push( { command: 'deck', text: 'Interact with deckofcards.api' } );

}
