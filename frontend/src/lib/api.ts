import axios from 'axios';

const api = axios.create({
  baseURL: '/api',
  headers: {
    'Content-Type': 'application/json',
  },
});

export const getAssets = () => api.get('/assets');
export const getAsset = (id: string) => api.get(`/assets/${id}`);
export const getDatacenters = () => api.get('/datacenters');
export const getChanges = () => api.get('/changes');

export default api;
