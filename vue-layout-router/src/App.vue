<script setup>

</script>

<template>

  <section id="layout">

    <header>
      <h1>Meus projetos</h1>
    </header>

    <aside>
      <nav>
        <router-link to="/">Home</router-link>
        <router-link to="/product">Produtos</router-link>
        <router-link to="/contact">Contatos</router-link>
        <router-link to="/about">Sobre nós</router-link>
      </nav>
    </aside>

    <main>
      <router-view></router-view>
    </main>

  </section>
  
</template>

<style scoped>

#layout {
    font-family: Helvetica, Arial, sans-serif;
    min-height: 100vh;
    width: 100vw;
    display: grid;
    grid-template-columns: 1fr 11fr;
    grid-template-rows: auto 1fr;

    grid-template-areas:
      'sidebar header'
      'sidebar main';
  }

  header {
    grid-area: header;
    height: 10vh;
    background-color: rgb(80, 160, 252);
  }

  aside {
    grid-area: sidebar;
    background-color: rgb(143, 45, 255);
  }

  aside nav {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    padding: 1rem;
  }

  main {
    grid-area: main;
  }

</style>
