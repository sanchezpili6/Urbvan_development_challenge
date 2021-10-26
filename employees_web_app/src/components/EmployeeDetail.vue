<template>
  <v-card rounded="xl" class="text--text">
    <v-card-title class="my-3">
      <h2>Nombre: {{ name}} {{last_name}}</h2>
    </v-card-title>
    <v-card-subtitle class="card-subtitle text--text">
      <h2>Número de {{employee()}}: {{id}}</h2>
      <h2>Puesto: {{job_position}}</h2>
      <h2>RFC: {{rfc}}</h2>
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
      <v-btn class="accent text--text" @click="edit()"><h4>Editar</h4></v-btn>
      <v-btn class="primary text--text" @click="deleteEmployee()"><h4>Dar de baja</h4></v-btn>
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
    notes:[],
    name:'',
    last_name:'',
  }),
  props:['Id'],
  async created(){
    let employeeId = this.$route.query.Id;
    axios.get(`http://localhost:3000/notes/${employeeId}`)
    axios.get(`http://localhost:3000/employee/${employeeId}`)
        .then(response => this.name = response.data['name'])
    axios.get(`http://localhost:3000/employee/${employeeId}`)
        .then(response => this.last_name = response.data['last_name'])
  },
  methods:{
    edit(){},
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
