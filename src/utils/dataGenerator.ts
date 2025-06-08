
export const generateRandomData = () => {
  const generateTimeSeriesData = (baseValue: number, variance: number, points: number = 6) => {
    const times = ['00:00', '04:00', '08:00', '12:00', '16:00', '20:00'];
    return times.slice(0, points).map((time, index) => ({
      time,
      value: Math.round((baseValue + (Math.random() - 0.5) * variance) * 100) / 100
    }));
  };

  const generateRadarData = () => {
    const subjects = ['North', 'East', 'South', 'West', 'Center'];
    return subjects.map(subject => ({
      subject,
      value: Math.round((60 + Math.random() * 40) * 100) / 100
    }));
  };

  return {
    temperature: generateTimeSeriesData(20, 8),
    humidity: generateTimeSeriesData(45, 20),
    pressure: generateRadarData(),
    energy: generateTimeSeriesData(70, 30),
    metrics: {
      temperature: Math.round((15 + Math.random() * 15) * 10) / 10,
      humidity: Math.round((20 + Math.random() * 20) * 10) / 10,
      pressure: Math.round((15 + Math.random() * 10) * 10) / 10,
      energy: Math.round((70 + Math.random() * 30) * 10) / 10
    }
  };
};
