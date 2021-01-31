const { BotkitConversation } = require("botkit");
const axios = require("axios");

module.exports = function(controller) {
    const convo = new BotkitConversation('deck_function', controller);

    convo.ask('What is your name?', async(response, convo, bot) => {
     //   performCall(response).then(await bot.say);
        
        const result = await(performCall(response));
        await bot.say( 'The deck id is ' + result );
        await convo.stop();
    }, 'name');

    
    controller.addDialog( convo );

    controller.hears( 'deck_function', 'message,direct_message', async ( bot, message ) => {
        await bot.beginDialog( 'deck_function' );
    });

    controller.commandHelp.push( { command: 'deck_function', text: 'Interact with deckofcards.api' } );

    async function performCall( selection ) {
        let response = await(axios.get('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1'));
        let deck_id = response.data.deck_id;
        return deck_id;
    }
}


