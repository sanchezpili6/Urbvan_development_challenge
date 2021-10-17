import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';

Vue.use(Vuetify);

export default new Vuetify({
    theme: {
        themes: {
            light: {
                primary: '#f1404b',
                secondary: '#380E10',
                accent: '#fbb100',
                text: '##0f1033',
            },
        },
    },
});
