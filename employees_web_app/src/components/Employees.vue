<template>
  <v-card color="primary" class="text--white" rounded="xl">
    <v-card-title>
      <v-text-field
          v-model="search"
          append-icon="mdi-magnify"
          label="Search"
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
          itemsPerPageText: 'Filas por página'
        }"
    ></v-data-table>
  </v-card>
</template>

<script>
export default {
  name: "Employees.vue",
  data () {
    return {
      search: '',
      headers: [
        { text: 'Id', filterable: true, value: 'id' },
        { text: 'Nombre', filterable: true, value: 'name',},
        { text: 'Apellidos', filterable: true, value: 'lastName' },
        { text: 'Fecha de ingreso',  filterable: false, value: 'startDate' },
        { text: 'Cumpleaños', filterable: true, value: 'birthday' },
        { text: 'Puesto', filterable: true, value: 'position' },
      ],
      employees: [
        {
          id: 1,
          name: 'María del Pilar',
          lastName: 'Sánchez Castillejos',
          startDate: '25/10/2021',
          birthday: '18 abril',
          position: 'mid backend developer',
        },
        {
          id: 2,
          name: 'Karla Stephania',
          lastName: 'López',
          startDate: '25/10/2021',
          birthday: '18 abril',
          position: 'mid backend developer',
        },
        {
          id: 3,
          name: 'María del Pilar',
          lastName: 'Sánchez Castillejos',
          startDate: '25/10/2021',
          birthday: '18 abril',
          position: 'mid backend developer',
        },
        {
          id: 4,
          name: 'María del Pilar',
          lastName: 'Sánchez Castillejos',
          startDate: '22/10/2021',
          birthday: '18 abril',
          position: 'mid backend developer',
        },
        {
          id: 5,
          name: 'María del Pilar',
          lastName: 'Sánchez Castillejos',
          startDate: '25/10/2020',
          birthday: '18 abril',
          position: 'mid backend developer',
        },
      ],
    }
  },
}
</script>

<style scoped>

</style>
