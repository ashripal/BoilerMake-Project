import { StatusBar } from 'expo-status-bar';
import React, {useState, useEffect} from 'react';
import { StyleSheet, Text, View, Button, Image } from 'react-native';
import { Camera } from 'expo-camera'
import RCTSafeAreaViewNativeComponent from 'react-native/Libraries/Components/SafeAreaView/RCTSafeAreaViewNativeComponent';

export default function App() {
  const [permissionCam, setPermissionCam] = useState(null);
  const [cam, setCam] = useState(null);
  const [img, setImg] = useState(null);
  const [type, setType] = useState(Camera.Constants.Type.backgroundColor);
 
  useEffect(() => {
      (async () => {
        const camStatus = await Camera.requestCameraPermissionsAsync();
        setHasCameraPermission(camStatus.status === 'granted');
      })();
  }, []);

  const getPic = async () => {
    if (cam) {
      const data = await cam.takePictureAsync(null);
      setImg(data.uri);
    }
  }

  if (permissionCam === false) {
    return <Text>Camera cannot be accessed.</Text>;
  }

  return (
    <View style={{flex:1}}>
      <View style = {styles.cameraContainer}>
        <Camera ref = {ref => setCamera(ref)}
        style = {styles.fixedRatio}
        type = {type}
        ratio = {'1:1'}
        />
      </View>
      <Button 
      title = "Flip Camera"
      press = {()=> {
        setType(type === Camera.Constants.Type.back ? Camera.Constants.Type.front : Camera.Constants.Type.back);
      }}>
      </Button>
      <Button title = "Capture Picture"
      onPress={() => takePicture()}
      />
      {image && <Image source = {{uri: img}} style = {{flex:1}} />}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    flexDirection:'row'
  },
  fixedRatio: {
    flex:1,
    aspectRatio:1
  }
});
