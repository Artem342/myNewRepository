<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const HidWorkList = ref([])

const getHidWorkList = async () => {
  let res = await axios.get('/hid_works/hid_work-json/')
  HidWorkList.value = res.data
}
onMounted(() => {
  getHidWorkList()
})

</script>


<template>
  <nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid">
    <a class="navbar-brand">Hidden Works</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="naFv-item">
          <a class="nav-link active" aria-current="page" href="#">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Features</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Pricing</a>
        </li>
        <li class="nav-item">
          <a class="nav-link disabled" aria-disabled="true">Disabled</a>
        </li>
      </ul>
    </div>
  </div>
  </nav>

  <div class="container">
    <div class="row">
        <form method="get" class="card card-body mb-4">
            <div class="row align-items-center">
                <div class="col-md-4">
                    <label>Рабочая документация</label>
                    <select id="working_documentation" name="working_documentation" class="form-select">
                        <option value="">Все</option>
                        <option value=""
                            {% if selected_working_documentation|add:"0" == doc.id %}selected{% endif %}>
                            {{ doc.designation }} - {{ doc.title }}
                        </option>
                        
                    </select>
                </div>
                <div class "col-2">
                    <button type="submit" class="btn btn-primary">показать</button>
                    <a href="">сбросить</a>
                </div>
            </div>
        </form>
            <div class="col-4">
                <div class="card" style="width: 18rem;">
                    <div class="card-body">
                        <h5 class="card-title">{{ hid_work.title }}</h5>
                        <p class="card-text">{{ hid_work.responsible_person_profile }}</p>
                        <p class="card-text">{{ hid_work.working_documentation.designation }}</p>
                        <a href={% url "hid_work-detail" hid_work.slug %} class="btn btn-primary">К скрытой работе</a>
                    </div>
                </div>
            </div>
    </div>
</div>
</template>


<style>

</style>