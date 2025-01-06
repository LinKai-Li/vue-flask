import axios from "axios";

const state = {
  games: [],
  stat: {},
};

const getters = {
  allGames: (state) => state.games,
};

const actions = {
  async getGames({ commit }) {
    try {
      const response = await axios.get("http://localhost:8000/games");
      commit("setGames", response.data.games);
    } catch (error) {
      console.error(error);
    }
  },

  async getStat({ commit }) {
    try {
      const response = await axios.get("http://localhost:8000/games/stats");
      commit("setStat", response.data);
    } catch (error) {
      console.error(error);
    }
  },

  async addGame({ commit }, game) {
    try {
      const response = await axios.post("http://localhost:8000/games", game);
      commit("newGame", response.data.game);
    } catch (error) {
      console.error(error);
    }
  },

  async updateGame({ commit }, updatedGame) {
    try {
      const response = await axios.put(
        `http://localhost:8000/games/${updatedGame.id}`,
        updatedGame,
      );
      commit("updateGame", response.data.game);
    } catch (error) {
      console.error(error);
    }
  },

  async deleteGame({ commit }, id) {
    try {
      await axios.delete(`http://localhost:8000/games/${id}`);
      commit("removeGame", id);
    } catch (error) {
      console.error(error);
    }
  },
};

const mutations = {
  setGames: (state, games) => (state.games = games),
  newGame: (state, game) => state.games.push(game),
  removeGame: (state, id) =>
    (state.games = state.games.filter((game) => game.id !== id)),
  updateGame: (state, updGame) => {
    const index = state.games.findIndex((game) => game.id === updGame.id);
    if (index !== -1) {
      state.games.splice(index, 1, updGame);
    }
  },
  setStat: (state, stat) => (state.stat = stat),
};

export default {
  state,
  getters,
  actions,
  mutations,
};
