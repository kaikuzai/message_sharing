import { useState, useEffect } from "react"
import apiClient from "../services/api-client"
import { AxiosError } from "axios";

interface MessageCounter {
    length: number;
};

const useMessageCounter = () => {
    const [data, setData] = useState<MessageCounter>();
    const [isLoading, setIsLoading] = useState<boolean>(true);
    const [error, setError] = useState<AxiosError | null>(null)

    useEffect(() => {
        const fetchData = async () => {
            try {
              const response = await apiClient.get<MessageCounter>("MessageCounter")
              setData(response.data)
            } catch (error) {
              setError(error as AxiosError)
            } finally {
              setIsLoading(false)
            } 
        }; 
        fetchData();
    }, []);

    return {data, isLoading, error};
}; 
export default useMessageCounter;