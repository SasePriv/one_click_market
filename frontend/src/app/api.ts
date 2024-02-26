import { SEARCH_SCRAPPER } from '@/constants';
import axios from 'axios';

export  const postSearch = async (searchSerializer: { text: string }) => axios.post(SEARCH_SCRAPPER(), searchSerializer)
