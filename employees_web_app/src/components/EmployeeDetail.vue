<template>
  <v-card rounded="xl" class="text--text">
    <v-card-title class="my-3">
      <h2>Nombre: {{ name }} {{last_name}}</h2>
    </v-card-title>
    <v-card-subtitle class="card-subtitle text--text">
      <h2>Número de {{employee()}}: {{id}}</h2>
      <h2>Puesto: {{job_position}}</h2>
      <h2>Fecha de entrada: {{start_date}}</h2>
      <h2>Cumpleaños: {{birthday}}</h2>
    </v-card-subtitle>
    <v-card v-for="(note, n) in notes" :key="n" class="my-3 mx-3 text notes">
      <v-card-title>
        <h1>
          {{note.title}}
        </h1>
      </v-card-title>
      <v-card-text>
        <h3>
          {{note.content}}
        </h3>
      </v-card-text>
    </v-card>
    <v-card-actions>
      <v-spacer></v-spacer>
      <AddNote/>
      <v-btn class="accent text--text">Editar</v-btn>
      <v-btn class="primary text--text">Dar de baja</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import AddNote from "./AddNote";
import axios from "axios";
export default {
  name: "EmployeeDetail.vue",
  components:{
    AddNote
  },
  data: () => ({
    notes:[]
  }),
  props:{
    id: String,
    name: String,
    rfc: String,
    last_name: String,
    start_date: String,
    birthday: String,
    job_position: String,
    pronouns: String
  },
  mounted(){
    axios.get(`http://localhost:3000/notes${this.id}`)
        .then(response => this.notes = response.data)
  },
  methods:{
    employee(){
      if(this.pronouns == 'Ella'){
        return 'empleada';
      }
      else if(this.pronouns =='Él'){
        return 'empleado';
      }
      else{
        return 'empleade';
      }
    }
  }
}
</script>

<style scoped>
  .card-subtitle{
    line-height: 200%;
  }
  .notes h1,h3{
    color: white;
  }
</style>
