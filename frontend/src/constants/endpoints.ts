import { API, PORT, DOMAIN, PROTOCOL } from './settings';

export const API_URL = () => `${PROTOCOL}://${DOMAIN}:${PORT}/${API}`;

// Endpoints
export const SEARCH_SCRAPPER = () => `${API_URL()}/${process.env.NEXT_PUBLIC_APP_MASTER_SCRAPPER}`;