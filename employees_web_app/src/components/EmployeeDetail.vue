<template>
  <v-card rounded="xl" class="text--text">
    <v-card-title class="my-3">
      <h2>Nombre: {{ name }} {{lastName}}</h2>
    </v-card-title>
    <v-card-subtitle class="card-subtitle">
      <h2>Número de {{employee()}}: {{id}}</h2>
      <h2>Puesto: {{position}}</h2>
      <h2>Fecha de entrada: {{startDate}}</h2>
      <h2>Cumpleaños: {{birthday}}</h2>
    </v-card-subtitle>
    <v-card v-for="(note, n) in notes" :key="n" class="my-3 mx-3 accent">
      <v-card-title>
        {{note.title}}
      </v-card-title>
      <v-card-subtitle>
        {{note.date}}
      </v-card-subtitle>
      <v-card-text>
        {{note.content}}
      </v-card-text>
    </v-card>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn class="accent text--text">Editar</v-btn>
      <v-btn class="primary text--text">Dar de baja</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: "EmployeeDetail.vue",
  props:{
    id: String,
    name: String,
    lastName: String,
    startDate: String,
    birthday: String,
    position: String,
    pronouns: String
  },
  data: () => ({
    notes:[
        {title: 'Nota 1', content: 'Contenido 1', date: '17/Octubre/2021'},
        {title: 'Nota 2', content: 'Contenido 2', date: '17/Octubre/2021'},
        {title: 'Nota 3', content: 'Contenido 3', date: '17/Octubre/2021'},
        {title: 'Nota 4', content: 'Contenido 4', date: '17/Octubre/2021'},
    ]
  }),
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
</style>
