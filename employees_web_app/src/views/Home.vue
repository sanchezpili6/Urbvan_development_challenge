<template>
  <v-app class="my-3 mx-3">
    <v-row>
      <v-col cols="5">
        <Employees v-on:childToParent="onPatientClick"/>
      </v-col>
      <v-col>
        <EmployeeDetail :id="id" :name="name" :lastName="lastName" :startDate="startDate" :birthday="birthday" :position="position"/>
      </v-col>
    </v-row>
  </v-app>
</template>

<script>
  import Employees from "../components/Employees";
  import EmployeeDetail from "../components/EmployeeDetail";
  export default {
    name: 'Home',

    components: {
      Employees,
      EmployeeDetail
    },
    data: () => ({
      id: '',
      name: '',
      lastName:'',
      startDate:'',
      birthday:'',
      position:''
    }),
    methods:{
      onPatientClick(id, name, lastName, startDate, birthday, position){
        this.id=id;
        this.name=name;
        this.lastName=lastName;
        this.startDate=startDate;
        this.birthday=birthday;
        this.position=position;
      }
    }
  }
</script>

<style>

</style>
