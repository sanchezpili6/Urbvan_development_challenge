<template>
  <v-container>
    <!-- add button -->
    <v-btn
        color="primary"
        @click="overlay=!overlay"
    >
      <v-icon size="50px">mdi-plus</v-icon>
    </v-btn>

    <!-- add note card -->

    <v-overlay :value="overlay" z-index=  "1">
      <v-card
          elevation="2"
          rounded="xl"
          color="primary"
          height="700"
          width="900"
      >
        <v-card-title justify="center">
          <v-spacer></v-spacer>
          <h1 style="font-size: 40px">CREAR NUEVA NOTA</h1>
          <v-spacer></v-spacer>
          <v-btn fab color="white" small @click="overlay=!overlay"><v-icon color="accent">mdi-close-thick</v-icon></v-btn>
        </v-card-title>
        <v-card-text>
            <form @submit.prevent="submit" v-model="isValid">
              <v-row>
                <v-spacer></v-spacer>
                <v-text-field v-model="form.title" class="note" outlined label="Título de la nota" :rules="titleRules"></v-text-field>
                <v-spacer></v-spacer>
              </v-row>
              <v-row>
                <v-spacer></v-spacer>
                <v-textarea v-model="form.content" class="note" :rules="contentRules" full-width outlined height="400" label="Escribe el contenido de tu nota aquí..."></v-textarea>
                <v-spacer></v-spacer>
              </v-row>
              <v-row justify="center">
                <v-btn color="accent" :disabled="!isValid" type="submit">
                  <h2 class="text--text">Guardar Nota</h2>
                </v-btn>
              </v-row>
            </form>
        </v-card-text>
      </v-card>
    </v-overlay>
  </v-container>
</template>

<script>
import axios from "axios";
export default {
  name: "AddEmployee",
    data: () =>({
      overlay: false,
      form:{
        title:'',
        content:'',
      },

      isValid: true,
      titleRules:[
        value => !!value || 'Se necesita un título'
      ],
      contentRules:[
        value => !!value ||'Necesitas agregar contenido'
      ]
    }),
    methods: {
      submit() {
        let employeeId = this.$route.query.Id;
        this.overlay = false
        const data = {"id":employeeId, "title": this.form.title, "content": this.form.content};

        axios.post('http://localhost:3000/notes/add', data)
            .then(function (response) {
              console.log(JSON.stringify(response.data));
            })
        location.reload()
      },
      employee(){
        if(this.pronouns == 'Ella'){
          return 'Empleada';
        }
        else if(this.pronouns =='Él'){
          return 'Empleado';
        }
        else{
          return 'Empleade';
        }
      },
      onButtonClick() {
        window.addEventListener('focus', () => {
        }, { once: true })
      },
    },
}
</script>

<style scoped>
.add{
  border-radius: 50%;
}
.note .error--text{
  color: #f96767 !important;
  caret-color: #f96767 !important;
}

</style>
