import { AxiosError } from "axios";
import { useState, useEffect } from "react";
import apiClient from "../services/api-client";

interface Welcome {
    reply: string;
}

const useWelcome = () => {
    const [data, setData] = useState<Welcome>();
    const [error, setError] = useState<AxiosError | null>(null);
    const [isLoading, setIsLoading] = useState<boolean>(true);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await apiClient.get<Welcome>("/Welcome")
                const formattedResponse = response.data
                setData(formattedResponse)
            } catch (error) {
                setError(error as AxiosError)
            } finally {
                setIsLoading(false)
            }
        }
        fetchData();
        console.log("Welcome fetched?")
    }, []);

    return {data, error, isLoading}
}

export default useWelcome; 