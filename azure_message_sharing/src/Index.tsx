import useMessageCounter from './hooks/useCounter'



const AppIndex = () => {

    const {data: messageAmount} = useMessageCounter();

    console.log("logging message amount",messageAmount);
    console.log("logging message amount lenght",messageAmount?.length);
  return (
    <>
    <h1>Welcome to Message Share!</h1>
    <h2>Currently we have</h2>
    <h2> {messageAmount?.length || 'thinking..'}</h2>
    <h2>messages</h2>
    </>
  )
}

export default AppIndex