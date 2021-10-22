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
        { text: 'Pronombres', filterable: true, value: 'pronouns'}
      ],
      employees: [
        {
          id: 1,
          name: 'María del Pilar',
          lastName: 'Sánchez Castillejos',
          startDate: '25/10/2021',
          birthday: '18 abril',
          position: 'mid backend developer',
          pronouns: 'Ella'
        },
        {
          id: 3,
          name: 'Rafita',
          lastName: 'Barajas ',
          startDate: '25/10/2021',
          birthday: '17 Octubre',
          position: 'mid backend developer',
          pronouns: 'Él'
        },
        {
          id: 4,
          name: 'Dani',
          lastName: 'Castañeda',
          startDate: '22/10/2021',
          birthday: '10 marzo',
          position: 'mid backend developer',
          pronouns: 'Él'
        },
      ],
    }
  },
  methods:{
    handleClick(e) {
      this.$emit('childToParent', e.id, e.name, e.lastName, e.startDate, e.birthday, e.position, e.pronouns)
    }
  }
}
</script>

<style scoped>

</style>
