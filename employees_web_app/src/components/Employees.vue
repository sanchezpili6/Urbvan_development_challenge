<template>
  <v-card color="primary" class="text--white" rounded="xl">
    <v-card-title>
      <v-text-field
          v-model="search"
          append-icon="mdi-magnify"
          label="Buscar"
          single-line
          hide-details
      ></v-text-field>
    </v-card-title>
    <v-data-table
        :headers="headers"
        :items="employees"
        :search="search"
        class="text--text"
        :footer-props="{
          showFirstLastPage: true,
          itemsPerPageText: 'Filas por página',
          itemsPerPageAllText: 'Todas'
        }"
        @click:row="handleClick"
    ></v-data-table>
  </v-card>
</template>

<script>
import axios from "axios";
export default {
  name: "Employees.vue",
  data () {
    return {
      search: '',
      headers: [
        { text: 'Id', filterable: true, value: 'id' },
        { text: 'RFC', filterable: true, value: 'rfc' },
        { text: 'Nombre', filterable: true, value: 'name',},
        { text: 'Apellidos', filterable: true, value: 'last_name' },
        { text: 'Fecha de ingreso',  filterable: false, value: 'start_date' },
        { text: 'Cumpleaños', filterable: true, value: 'birthday' },
        { text: 'Puesto', filterable: true, value: 'job_position' },
        { text: 'Pronombres', filterable: true, value: 'pronouns'}
      ],
      employees: []
    }
  },
  mounted (){
    axios.get('http://localhost:3000/employee',)
        .then(response => this.employees = response.data)
  },
  methods:{
    handleClick(e) {
      this.$emit('childToParent', e.id, e.rfc, e.name, e.last_name, e.start_date, e.birthday, e.job_position, e.pronouns)
    }
  }
}
</script>

<style scoped>

</style>
