<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { HidWork, HidWorkMaterial, WorkDoc } from '@/api.js'
import NavBar from '@/components/NavBar.vue'

const HidWorkList = ref([])
const material = ref([])
const search = ref('')
const selectedWorkingDocumentation = ref('')
const workingDocs = ref([])

const workDoc = ref([])
const getWorkDoc = async () => {
  workDoc.value - (await WorkDoc.getList()).data
}

const getHidWorkList = async () => {
  let res = await HidWork.getList({search: search.value})
  console.log(res)
  HidWorkList.value = res.results
  let res2 = await HidWorkMaterial.getList()
  material.value = res2.results
}
onMounted(() => {
  getHidWorkList()
})

const getWorkingDocs = async () => {
  try {
    let res = await axios.get('/api/working-documentation/') // Замените на правильный URL
    workingDocs.value = res.data
  } catch (error) {
    console.error('Error fetching working docs:', error)
  }
}

const resetFilters = () => {
  selectedWorkingDocumentation.value = ''
  // Добавьте логику сброса других фильтров
}

onMounted(() => {
  getHidWorkList()
  getWorkingDocs()
})
</script>

<template>
  <NavBar/>
  
  {{ material }}
  <div class="container">
    <div class="row">
      <input v-model="search" @input="getHidWorkList()">
      <form method="get" class="card card-body mb-4" @submit.prevent>
        <div class="row align-items-center">
          <div class="col-md-4">
            <label>Рабочая документация</label>
            <select 
              id="working_documentation" 
              name="working_documentation" 
              class="form-select"
              v-model="selectedWorkingDocumentation"
            >
              <option value="">Все</option>
              <option 
                v-for="doc in workingDocs" 
                :key="doc.id"
                :value="doc.id"
                :selected="selectedWorkingDocumentation == doc.id"
              >
                {{ doc.designation }} - {{ doc.title }}
              </option>
            </select>
          </div>
          <div class="col-2">
            <button type="submit" class="btn btn-primary">показать</button>
            <a href="#" @click.prevent="resetFilters">сбросить</a>
          </div>
        </div>
      </form>

      <div class="col-4" v-for="hid_work in HidWorkList" :key="hid_work.id">
        <div class="card" style="width: 18rem;">
          <div class="card-body">
            <h5 class="card-title">{{ hid_work.title }}</h5>
            <p class="card-text">{{ hid_work.responsible_person_profile }}</p>
            <p class="card-text">{{ hid_work.working_documentation?.designation || '' }}</p>
            <a 
              :href="`/hid_works/${hid_work.slug}/`" 
              class="btn btn-primary"
            >
              К скрытой работе
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* Добавьте свои стили здесь */
</style>