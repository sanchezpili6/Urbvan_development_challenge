<template>
  <v-app class="my-3 mx-3">
    <v-row>
      <v-col cols="5">
        <Employees v-on:childToParent="onPatientClick"/>
      </v-col>
      <v-col>
        <EmployeeDetail :id="id" :name="name" :lastName="lastName" :startDate="startDate" :birthday="birthday" :position="position" :pronouns="pronouns"/>
      </v-col>
    </v-row>
    <AddEmployee/>
  </v-app>
</template>

<script>
  import Employees from "../components/Employees";
  import EmployeeDetail from "../components/EmployeeDetail";
  import AddEmployee from "../components/AddEmployee";
  export default {
    name: 'Home',

    components: {
      Employees,
      EmployeeDetail,
      AddEmployee
    },
    data: () => ({
      id: '',
      name: '',
      lastName:'',
      startDate:'',
      birthday:'',
      position:'',
      pronouns: ''
    }),
    methods:{
      onPatientClick(id, name, lastName, startDate, birthday, position, pronouns){
        this.id=id;
        this.name=name;
        this.lastName=lastName;
        this.startDate=startDate;
        this.birthday=birthday;
        this.position=position;
        this.pronouns=pronouns;
      }
    }
  }
</script>

<style>

</style>
