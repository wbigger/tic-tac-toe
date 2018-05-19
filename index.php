<?php

$method = $_SERVER["REQUEST_METHOD"];

switch($method){
	case "POST":
		post();
		break;
	case "GET":
		echo 'Get';
		break;
}



function post(){
	if(isset($_POST['data'])){
		try{
			$db = new PDO('mysql:host=localhost;dbname=raspberry_server', 'root', '');
			echo 'connessione database effettuata';	
        	}catch(PDOException $e){
			echo $e->getMessage();
			exit();
		}
		$data = (int) $_POST['data'];
        	echo 'e stato premuto il bottone' . $data;
		db_insert($db, $data);
	}else
		echo 'non ricevuto';

}

function db_insert($db, $data){
	try{
		$db->beginTransaction();
		$sql = 'INSERT into raspberry_server values :data';
		$stmt = $db->prepare($sql);
		$stmt->bindParam(':data', $data);
		$stmt->execute();
		echo 'dati inseriti correttamente';
	}catch(PDOException $e){
		echo $e->getMessage();
		$db->rollBack()
	}

}
?>









